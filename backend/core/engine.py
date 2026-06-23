from modules.duplicates import remove_duplicates
from modules.nulls import remove_nulls
from modules.cpf_validator import validate_cpf_column
from modules.date_formatter import standardize_dates
from modules.email_validator import validate_email_column
from modules.phone_formatter import format_phone_column
from modules.encoding_fixer import fix_encoding_column
from modules.text_cleaner import clean_text_column
from modules.outlier_detector import detect_outliers
from modules.cnpj_validator import validate_cnpj_column
from modules.cep_validator import validate_cep_column

TOOLS = {
    "duplicates": remove_duplicates,
    "nulls": remove_nulls,
    "cpf": validate_cpf_column,
    "dates": standardize_dates,
    "email": validate_email_column,
    "phone": format_phone_column,
    "encoding": fix_encoding_column,
    "text_cleaner": clean_text_column,
    "outlier": detect_outliers,
    "cnpj": validate_cnpj_column,
    "cep": validate_cep_column
}


class ETLEngine:

    @staticmethod
    def run(df, operations, config=None):

        config = config or {}

        print("Operações recebidas:", operations)

        for operation in operations:

            print(f"Executando: {operation}")

            if operation in TOOLS:

                df = TOOLS[operation]( df, config.get(operation, {}))

            else:
                print(f"Ferramenta não encontrada: {operation}")

        return df