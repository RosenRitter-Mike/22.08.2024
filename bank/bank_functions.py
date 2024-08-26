from datetime import datetime, timedelta
import pprint
def init_bank_accounts() -> dict:

    '''
    Initialize the bank accounts data structure.
    :return:
    The bank accounts data structure (dict[any]) that includes the account data
    '''

    bank_accounts: dict = {
        1001: {
            "first_name": "Alice",
            "last_name": "Smith",
            "id_number": "123456789",
            "balance": 2500.50,
            "transactions_to_execute": [
                ("2024-08-17 14:00:00", 1001, 1002, 300), ("2024-08-17 15:00:00", 1001, 1003, 200)],
            "transaction_history": [
                ("2024-08-15 09:00:00", 1001, 1002, 500), ("2024-08-15 09:30:00", 1001, 1003, 100)]
        },
        1002: {
            "first_name": "Bob",
            "last_name": "Johnson",
            "id_number": "987654321",
            "balance": 3900.75,
            "transactions_to_execute": [],
            "transaction_history": []
        }}
    return bank_accounts;

def new_transaction(bank_accounts: dict) -> None:
    '''
    Create a new transaction for an account.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''


    while True:
        try:
            send: int = int(input("sender account number: "));
            if send not in bank_accounts:
                print(f"sender account- {send} - could not be found");
                continue;
            rec: int = int(input("recipient account number: "));

            if rec not in bank_accounts:
                print(f"recipient account- {rec} - could not be found");
                continue;
            tr_sum: float = float(input("sum of transfer: "));

            if bank_accounts[send]["balance"] < tr_sum:
                print(f"sender account balance- {bank_accounts[send]['balance']}\nthe transfer sum - {tr_sum}\n"
                      f"not enough balance");
                continue;
            else:
                temp_t: tuple = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), send, rec, tr_sum);
                bank_accounts[send]["transactions_to_execute"].append(temp_t);
        except TypeError as e:
            print(f"{str(e)} - is not a valid input");

        except Exception as e:
            print(f"{e} - error has occurred");

def commit_transactions(bank_accounts: dict) -> None:
    '''
    Commit the planed transactions for the given account.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''
    while True:
        try:
            acc: int = int(input("account number: "));
            if acc not in bank_accounts:
                print(f"account- {acc} - could not be found");
                continue;
            transactions_pending: list[any] = bank_accounts[acc]["transactions_to_execute"][:];
            for tra in transactions_pending:
                bank_accounts[acc]['balance'] -= tra[3];
                bank_accounts[tra[2]]['balance'] += tra[3];
                bank_accounts[acc]["transaction_history"].append(tra);
                bank_accounts[acc]["transactions_to_execute"].remove(tra);
            else:
                print(f"account data\n{bank_accounts[acc]}");
        except TypeError as e:
            print(f"{str(e)} - is not a valid input");

        except Exception as e:
            print(f"{e} - error has occurred");



def find_by_id(bank_accounts: dict) -> None:
    '''
    Find an account by users id number. And display its data.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    try:
        id_num: int = int(input("id number: "));
        for key in bank_accounts.keys():
            if bank_accounts[key]["id_number"] == str(id_num):
                print(bank_accounts[key]);
    except TypeError as e:
        print(f"{str(e)} - is not a valid input");

    except Exception as e:
        print(f"{e} - error has occurred");

def find_by_name(bank_accounts: dict) -> None:
    '''
    Find an account by users name or part of it. And display its data.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    name: str = input("first name: ");
    for key in bank_accounts.keys():
        if name.lower() in bank_accounts[key]["first_name"].lower():
            print(bank_accounts[key]);

def accounts_sorted_by_balance(bank_accounts: dict) -> None:
    '''
    Display all accounts data sorted by balance.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    acc_list: list = sorted(bank_accounts.keys(), key= lambda acc: bank_accounts[acc]['balance']);
    for acc_n in acc_list:
        pprint.pprint(bank_accounts[acc_n]);


def accounts_with_negative_balance(bank_accounts: dict) -> None:
    '''
    Display data of the accounts with negative balance.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    for key in bank_accounts.keys():
        if bank_accounts[key]["balance"] < 0:
            print(bank_accounts[key]);

def accounts_balance_sum(bank_accounts: dict) -> None:
    '''
    Display the sum of all founds in the accounts (sum of account balances)
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    print(f"sum of all accounts: {sum(map(lambda key: bank_accounts[key]['balance'], bank_accounts))}");

def transactions_today(bank_accounts: dict) -> None:
    '''
    Display all of today's transactions (that were commited)
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    tod_tr: list = [];
    today: str = datetime.today().strftime('%Y-%m-%d');
    for key in bank_accounts.keys():
        for transaction in bank_accounts[key]["transaction_history"]:
            tr_date: list[str] = str(transaction[0]).split(' ')[0];
            print(tr_date);
            if tr_date == today:
                tod_tr.append(transaction);
    print(f"today's transactions:\n{tod_tr}");

def open_new_account(bank_accounts: dict) -> None:
    '''
    Open a new bank account.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    acc_num: int = max(bank_accounts.keys()) + 1;
    fname: str = input("first name: ");
    lname: str = input("last name: ");
    id_num: str = input("id number: ");
    try:
        bal: int = int(input("starting balance: "));

        new_acc: dict = {
            "first_name": fname,
            "last_name": lname,
            "id_number": id_num,
            "balance": bal,
            "transactions_to_execute": [],
            "transaction_history": []
        }

        bank_accounts[acc_num] = new_acc;
    except TypeError as e:
        print(f"{str(e)} - is not a valid input");

    except Exception as e:
        print(f"{e} - error has occurred");
    finally:
        print(f"{fname} {lname} - thanks for joining our bank!\nyour money is in good hands.")


def view_reports(bank_accounts: dict) -> None:
    '''
    Open the view reports menu. Allows report actions (such as: finding an account by id or name, or the display of all
    negative balance accounts, etc. )
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    print("===========Report Menu==============")
    print("0 - back to previous menu\n1 - print all\n2 - print account\n3 - find by id\n4 - find by name\n"
          "5 - print all accounts sorted by balance\n6 -  print all account with negative balance\n"
          "7 - print sum of all accounts\n8 - print transactions today");
    try:
        action: int = int(input("What is the purpose of your visit? "));
        while True:
            match action:
                case 0:
                    return;
                case 1:
                    pprint.pprint(bank_accounts);
                    return;
                case 2:
                    acc: int = int(input("account number: "));
                    if acc in bank_accounts.keys():
                        print(bank_accounts[acc]);
                    else:
                        print(f"account- {acc} - could not be found");
                    return;
                case 3:
                    find_by_id(bank_accounts);
                    return;
                case 4:
                    find_by_name(bank_accounts);
                    return;
                case 5:
                    accounts_sorted_by_balance(bank_accounts);
                    return;
                case 6:
                    accounts_with_negative_balance(bank_accounts);
                    return;
                case 7:
                    accounts_balance_sum(bank_accounts);
                    return;
                case 8:
                    transactions_today(bank_accounts);
                    return;
                case _:
                    print("invalid input");
                    continue;
    except TypeError as e:
        print(f"{str(e)} - is not a valid input");

    except Exception as e:
        print(f"{e} - error has occurred");
    finally:
        print("You are exiting the reports menu")

def main_menu(bank_accounts: dict) -> None:
    '''
    Opens the main manu of the bank. Allows main menu actions
    (such as: opening a new account, or creating a new transaction, etc. ).
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''
    
    # action: int = None;
    while True:
        print("===========Main Menu==============")
        print("0 - open new account\n1 - new transaction\n2 - commit all transactions\n3 - reports menu\n999 - exit");
        try:
            action: int = int(input("What is the purpose of your visit? "));
            match action:
                case 0:
                    open_new_account(bank_accounts);
                case 1:
                    new_transaction(bank_accounts);
                case 2:
                    commit_transactions(bank_accounts);
                case 3:
                    view_reports(bank_accounts);
                case 999:
                    print("leaving the system, have a nice day!")
                    break;
                case _:
                    print("invalid input");
                    continue;

            print();

        except TypeError as e:
            print(f"{str(e)} - is not a valid input");

        except Exception as e:
            print(f"{e} - error has occurred");
        finally:
            print("Dear client, we thank you for choosing our bank.\nHave a great day!")

# bank_ac = init_bank_accounts();
# accounts_balance_sum(bank_ac);