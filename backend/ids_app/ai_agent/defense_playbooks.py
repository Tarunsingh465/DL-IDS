# defense_playbooks.py

"""
========================================================
PHASE 6 — AI DEFENSE PLAYBOOK ENGINE
========================================================

This module contains attack-specific
AI cyber-defense playbooks.

Purpose:
✔ attack-specific mitigation
✔ autonomous containment logic
✔ adaptive defensive procedures
✔ SOC-style response templates
✔ mitigation policy generation

This introduces:
AI-driven cyber defense playbooks
========================================================
"""


class DefensePlaybookEngine:

    def __init__(self):

        """
        ====================================================
        PLAYBOOK DATABASE
        ====================================================
        """

        self.playbooks = {

            # ------------------------------------------------
            # DDOS PLAYBOOK
            # ------------------------------------------------

            "DDOS": [

                "Enable rate limiting",

                "Block malicious traffic sources",

                "Activate DDoS mitigation mode",

                "Monitor abnormal traffic spikes",

                "Escalate network monitoring"
            ],

            # ------------------------------------------------
            # SQL INJECTION PLAYBOOK
            # ------------------------------------------------

            "WEB_SQL_INJECTION": [

                "Inspect suspicious SQL queries",

                "Enable WAF protection rules",

                "Isolate vulnerable web endpoints",

                "Monitor database activity",

                "Escalate web application security"
            ],

            # ------------------------------------------------
            # XSS PLAYBOOK
            # ------------------------------------------------

            "WEB_XSS": [

                "Inspect malicious scripts",

                "Enable browser security protections",

                "Sanitize user input validation",

                "Monitor web session activity",

                "Escalate frontend monitoring"
            ],

            # ------------------------------------------------
            # PORTSCAN PLAYBOOK
            # ------------------------------------------------

            "PORTSCAN": [

                "Track reconnaissance activity",

                "Increase firewall sensitivity",

                "Monitor suspicious port activity",

                "Watch attacker behavior",

                "Escalate network visibility"
            ],

            # ------------------------------------------------
            # BRUTE FORCE PLAYBOOK
            # ------------------------------------------------

            "FTP_PATATOR": [

                "Enable account lockout policy",

                "Monitor authentication attempts",

                "Restrict repeated login failures",

                "Escalate identity monitoring"
            ],

            "SSH_PATATOR": [

                "Restrict SSH authentication attempts",

                "Enable SSH hardening policies",

                "Monitor remote access activity",

                "Escalate authentication monitoring"
            ],

            # ------------------------------------------------
            # HEARTBLEED PLAYBOOK
            # ------------------------------------------------

            "HEARTBLEED": [

                "Inspect OpenSSL vulnerabilities",

                "Patch vulnerable services",

                "Isolate affected systems",

                "Escalate critical infrastructure monitoring"
            ],

            # ------------------------------------------------
            # INFILTRATION PLAYBOOK
            # ------------------------------------------------

            "INFILTRATION": [

                "Isolate compromised host",

                "Investigate lateral movement",

                "Escalate incident response",

                "Activate containment procedures"
            ]
        }

    # ====================================================
    # GET DEFENSE PLAYBOOK
    # ====================================================

    def get_playbook(
        self,
        attack_type
    ):

        """
        Retrieve attack-specific playbook.
        """

        return self.playbooks.get(

            attack_type,

            [
                "Monitor suspicious activity",

                "Collect additional telemetry",

                "Escalate AI monitoring"
            ]
        )

    # ====================================================
    # GENERATE ADAPTIVE PLAYBOOK
    # ====================================================

    def generate_adaptive_playbook(

        self,

        attack_type,
        severity,
        repeat_offender=False
    ):

        """
        Generate adaptive AI defense playbook.
        """

        playbook = self.get_playbook(
            attack_type
        )

        adaptive_playbook = list(playbook)

        # ------------------------------------------------
        # HIGH SEVERITY ESCALATION
        # ------------------------------------------------

        if severity in [

            "HIGH",
            "CRITICAL"
        ]:

            adaptive_playbook.extend([

                "Increase defensive posture",

                "Enable enhanced monitoring"
            ])

        # ------------------------------------------------
        # REPEAT OFFENDER ESCALATION
        # ------------------------------------------------

        if repeat_offender:

            adaptive_playbook.extend([

                "Flag attacker as repeat offender",

                "Escalate autonomous restrictions"
            ])

        return {

            "attack_type":
            attack_type,

            "severity":
            severity,

            "adaptive_playbook":
            adaptive_playbook
        }# defense_playbooks.py

"""
========================================================
AI DEFENSE PLAYBOOK ENGINE
========================================================

This module simulates autonomous SOC-style
cyber defense playbooks.

Responsibilities:
✔ attack-specific mitigation plans
✔ automated response strategies
✔ SOC defensive workflows
✔ adaptive cyber defense orchestration
✔ incident containment procedures
"""

# --------------------------------------------------
# DEFENSE PLAYBOOK ENGINE
# --------------------------------------------------

class DefensePlaybookEngine:

    def __init__(self):

        """
        Stores generated playbooks.
        """

        self.playbook_history = []

    # --------------------------------------------------
    # GENERATE DEFENSE PLAYBOOK
    # --------------------------------------------------

    def generate_playbook(

        self,
        attack_type,
        severity,
        decision,
        defense_state
    ):

        """
        Generate adaptive defense playbook.
        """

        playbook_steps = []

        # --------------------------------------------------
        # COMMON INITIAL RESPONSE
        # --------------------------------------------------

        playbook_steps.extend([

            "Validate threat intelligence",

            "Analyze attacker behavior",

            "Correlate security events",

            "Update threat monitoring"
        ])

        # --------------------------------------------------
        # ATTACK-SPECIFIC PLAYBOOKS
        # --------------------------------------------------

        # DDOS
        if attack_type == "DDOS":

            playbook_steps.extend([

                "Enable DDoS mitigation mode",

                "Apply rate limiting",

                "Block malicious traffic sources",

                "Monitor network saturation",

                "Escalate to SOC team"
            ])

        # SQL INJECTION
        elif attack_type == "WEB_SQL_INJECTION":

            playbook_steps.extend([

                "Inspect malicious SQL queries",

                "Enable WAF protections",

                "Block suspicious requests",

                "Audit backend database logs",

                "Escalate web application monitoring"
            ])

        # PORTSCAN
        elif attack_type == "PORTSCAN":

            playbook_steps.extend([

                "Track reconnaissance activity",

                "Monitor targeted ports",

                "Enable enhanced firewall logging",

                "Flag suspicious scanning behavior"
            ])

        # XSS
        elif attack_type == "WEB_XSS":

            playbook_steps.extend([

                "Inspect injected scripts",

                "Enable browser protection policies",

                "Audit user input validation",

                "Monitor frontend traffic"
            ])

        # UNKNOWN ATTACK
        else:

            playbook_steps.extend([

                "Perform advanced threat hunting",

                "Enable anomaly monitoring",

                "Collect forensic telemetry",

                "Escalate investigation priority"
            ])

        # --------------------------------------------------
        # SEVERITY-BASED ACTIONS
        # --------------------------------------------------

        if severity == "CRITICAL":

            playbook_steps.extend([

                "Activate emergency defense mode",

                "Escalate incident severity",

                "Increase SOC monitoring",

                "Initiate containment procedures"
            ])

        elif severity == "HIGH":

            playbook_steps.extend([

                "Increase defensive monitoring",

                "Apply temporary restrictions",

                "Track lateral movement"
            ])

        # --------------------------------------------------
        # DECISION-BASED ACTIONS
        # --------------------------------------------------

        if decision == "BLOCK":

            playbook_steps.extend([

                "Permanently block attacker",

                "Blacklist attacker indicators"
            ])

        elif decision == "TEMP BAN":

            playbook_steps.extend([

                "Apply temporary containment",

                "Schedule automated review"
            ])

        elif decision == "MONITOR":

            playbook_steps.extend([

                "Continue behavioral monitoring",

                "Track future activity"
            ])

        # --------------------------------------------------
        # DEFENSE STATE ACTIONS
        # --------------------------------------------------

        if defense_state == "CRITICAL LOCKDOWN MODE":

            playbook_steps.extend([

                "Restrict external connectivity",

                "Enable maximum IPS sensitivity",

                "Lock high-risk services"
            ])

        elif defense_state == "DEFENSE MODE":

            playbook_steps.extend([

                "Increase autonomous defense posture",

                "Enable advanced threat analytics"
            ])

        # --------------------------------------------------
        # FINAL PLAYBOOK
        # --------------------------------------------------

        playbook = {

            "attack_type":
            attack_type,

            "severity":
            severity,

            "decision":
            decision,

            "defense_state":
            defense_state,

            "playbook_steps":
            playbook_steps
        }

        # Save history
        self.playbook_history.append(
            playbook
        )

        return playbook

    # --------------------------------------------------
    # GET PLAYBOOK HISTORY
    # --------------------------------------------------

    def get_playbook_history(self):

        return self.playbook_history