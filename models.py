

class Asset:

    def __init__(self):
        self.biography = None
        self.maintenance_history = None
        self.assignment_history = []
        self.issues_of_note = []
        self.litigation_events = []

    def generate_csv(self):
        pass

class IssueOfNote:

    def __init__(self):
        self.issue_text = None
        self.level = None
        self.evidence = None

class Biography:

    def __init__(self):
        self.application_number = None
        self.publication_number = None
        self.grant_number = None

        self.priority_date = None
        self.publication_date = None
        self.grant_date = None

        self.original_assignee = None
        self.current_assignee =  None

        self.inventors = []

        self.USPC_Classifications = []
        self.IPC_Classifications = []
        self.CPC_Classifications = []

        self.priority_claims = []
        self.forward_citations = []
        self.backward_citations = []

        self.gov_source_link = None

class inventor:
    pass

class Assignment_Event:

    def __init__(self):
        self.reel = None
        self.frame = None

        self.execution_date = None
        self.record_date = None
        self.assignment_type = None

        self.assignor_name = None
        self.assignee_name = None
        self.assignee_address = None

        self.correspondent_name = None
        self.correspondent_address = None

        self.source_link = None



class MaintenenceHistory:

    def __init__(self):
        self.first_window_open = None
        self.first_window_late = None
        self.first_window_close = None
        self.first_window_payment_status = None

        self.second_window_open = None
        self.second_window_late = None
        self.second_window_close = None
        self.second_window_payment_status = None

        self.third_window_open = None
        self.third_window_late = None
        self.third_window_close = None
        self.third_window_payment_status = None

        self.source_link = None
        self.pdf_link = None

    def to_dict(self):
        pass




class LitigationEvents:

    def __init__(self):
        self.case_number = None
        self.title = None
        self.venue = None
        self.judge_name = None

        self.parties = []


    def add_party(self,party):
        self.parties.append(party)

class Party:

    def __init__(self):
        self.name = None
        self.address = None
        self.role = None