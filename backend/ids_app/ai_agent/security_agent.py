# security_agent.py

"""
Autonomous AI Security Agent

This module acts as the main AI brain
for the IDS/IPS platform.

Responsibilities:
- threat analysis
- memory tracking
- severity scoring
- IPS decisions
- recommendations
- attack explanations
- autonomous IPS orchestration
- attacker reputation analysis
- threat intelligence tracking
- incident response generation
- adaptive defense state management
- centralized AI action logging
- autonomous response orchestration
- adaptive AI defense playbooks
"""

# --------------------------------------------------
# IMPORT ENGINES
# --------------------------------------------------

from .severity_engine import (
    calculate_severity
)

from .threat_memory import (
    update_attacker_memory,
    is_repeat_offender
)

from .recommendation_engine import (
    generate_recommendation
)

from .explanation_engine import (
    generate_explanation
)

from .attack_normalizer import (
    normalize_attack_name
)

from .ips_engine import (
    IPSEngine
)

from .reputation_engine import (
    calculate_reputation
)

from .threat_intelligence import (
    ThreatIntelligenceEngine
)

from .incident_response import (
    generate_incident_report
)

from .defensive_state_engine import (
    DefensiveStateEngine
)

from .action_logger import (
    AIActionLogger
)

from .response_orchestrator import (
    ResponseOrchestrator
)

from .defense_playbooks import (
    DefensePlaybookEngine
)

from .system_enforcer import (
    SystemEnforcer
)

from .enforcement_policy_engine import (
    EnforcementPolicyEngine
)

from .containment_engine import (
    ContainmentEngine
)

from .incident_action_center import (
    IncidentActionCenter
)

# --------------------------------------------------
# GLOBAL ENGINE OBJECTS
# --------------------------------------------------

ips_engine = IPSEngine()

system_enforcer = (
    SystemEnforcer()
)

policy_engine = (
    EnforcementPolicyEngine()
)

incident_center = (
    IncidentActionCenter()
)

threat_intelligence = (
    ThreatIntelligenceEngine()
)

defensive_state_engine = (
    DefensiveStateEngine()
)

action_logger = (
    AIActionLogger()
)

response_orchestrator = (
    ResponseOrchestrator()
)

defense_playbook_engine = (
    DefensePlaybookEngine()
)

containment_engine = (
    ContainmentEngine()
)

# --------------------------------------------------
# MAIN AI ANALYSIS PIPELINE
# --------------------------------------------------

def analyze_threat(
    ip_address,
    attack_type,
    confidence
):

    """
    Analyze detected threat.

    Parameters:
    ip_address (str)
    attack_type (str)
    confidence (float)

    Returns:
    dict
    """

    # --------------------------------------------------
    # NORMALIZE ATTACK LABEL
    # --------------------------------------------------

    normalized_attack = normalize_attack_name(
        attack_type
    )

    # --------------------------------------------------
    # UPDATE ATTACKER MEMORY
    # --------------------------------------------------

    attacker_info = update_attacker_memory(
        ip_address,
        normalized_attack
    )

    # --------------------------------------------------
    # REPEAT OFFENDER DETECTION
    # --------------------------------------------------

    repeat_offender = is_repeat_offender(
        ip_address
    )

    # --------------------------------------------------
    # CALCULATE SEVERITY
    # --------------------------------------------------

    severity = calculate_severity(
        attack_type=normalized_attack,
        confidence=confidence,
        repeat_count=attacker_info[
            "attack_count"
        ]
    )

    # --------------------------------------------------
    # CALCULATE REPUTATION
    # --------------------------------------------------

    reputation_score, reputation_level = (
        calculate_reputation(
            severity=severity,
            attack_count=attacker_info[
                "attack_count"
            ],
            repeat_offender=repeat_offender
        )
    )

    # --------------------------------------------------
    # UPDATE THREAT INTELLIGENCE
    # --------------------------------------------------

    threat_intelligence.update_attacker_profile(
        ip_address=ip_address,
        attack_type=normalized_attack,
        severity=severity,
        reputation_score=reputation_score,
        reputation_level=reputation_level
    )

    # --------------------------------------------------
    # GET ATTACKER PROFILE
    # --------------------------------------------------

    attacker_profile = (
        threat_intelligence.get_attacker_profile(
            ip_address
        )
    )

    # --------------------------------------------------
    # AUTONOMOUS IPS ENGINE DECISION
    # --------------------------------------------------

    decision = ips_engine.decide_ips_action(
        ip_address=ip_address,
        severity=severity,
        attack_count=attacker_info[
            "attack_count"
        ],
        attack_type=normalized_attack
    )

    # --------------------------------------------------
    # ENFORCEMENT POLICY
    # --------------------------------------------------

    enforcement_policy = (

        policy_engine.generate_policy(

            attack_type=
            normalized_attack,

            severity=
            severity,

            decision=
            decision
        )
    )

    # --------------------------------------------------
    # CONTAINMENT ENGINE
    # --------------------------------------------------

    containment_record = (

        containment_engine
        .apply_containment(

            ip_address=
            ip_address,

            severity=
            severity,

            decision=
            decision
        )
    )

    # --------------------------------------------------
    # AUTONOMOUS ENFORCEMENT
    # --------------------------------------------------

    enforcement_result = (

        system_enforcer.enforce(

            ip_address=ip_address,

            decision=decision,

            severity=severity
        )
    )
    # --------------------------------------------------
    # INCIDENT MANAGEMENT
    # --------------------------------------------------

    incident = None

    if decision in [

        "TEMP BAN",

        "BLOCK"
    ]:

        incident = (

            incident_center.create_incident(

                ip_address=ip_address,

                attack_type=normalized_attack,

                severity=severity,

                decision=decision
            )
        )

    # --------------------------------------------------
    # IPS STATUS CHECKS
    # --------------------------------------------------

    is_watchlisted = (
        ip_address in ips_engine.watchlist_ips
    )

    is_temp_banned = (
        ip_address in ips_engine.temp_banned_ips
    )

    is_blocked = (
        ip_address in ips_engine.blocked_ips
    )

    # --------------------------------------------------
    # EVALUATE GLOBAL DEFENSE STATE
    # --------------------------------------------------

    critical_attackers = len(
        threat_intelligence.get_critical_attackers()
    )

    blocked_ips = len(
        ips_engine.get_blocked_ips()
    )

    temp_banned_ips = len(
        ips_engine.get_temp_banned_ips()
    )

    suspicious_attackers = len(
        ips_engine.get_watchlist()
    )

    defense_state = (
        defensive_state_engine
        .evaluate_defense_state(

            critical_attackers=
            critical_attackers,

            blocked_ips=
            blocked_ips,

            temp_banned_ips=
            temp_banned_ips,

            suspicious_attackers=
            suspicious_attackers
        )
    )

    # --------------------------------------------------
    # GENERATE RECOMMENDATION
    # --------------------------------------------------

    recommendation = generate_recommendation(
        attack_type=normalized_attack,
        severity=severity,
        repeat_offender=repeat_offender
    )

    # --------------------------------------------------
    # GENERATE EXPLANATION
    # --------------------------------------------------

    explanation = generate_explanation(
        normalized_attack
    )

    # --------------------------------------------------
    # GENERATE INCIDENT REPORT
    # --------------------------------------------------

    incident_report = (
        generate_incident_report(

            ip_address=ip_address,

            attack_type=normalized_attack,

            severity=severity,

            reputation_level=
            reputation_level,

            decision=decision,

            recommendation=
            recommendation
        )
    )

    # --------------------------------------------------
    # LOG AI ACTION
    # --------------------------------------------------

    action_logger.log_action(

        ip_address=ip_address,

        attack_type=normalized_attack,

        severity=severity,

        decision=decision,

        defense_state=defense_state,

        reputation_level=reputation_level
    )

    # --------------------------------------------------
    # GET RECENT AI LOGS
    # --------------------------------------------------

    recent_ai_logs = (
        action_logger.get_recent_logs()
    )

    # --------------------------------------------------
    # GENERATE AUTONOMOUS RESPONSE WORKFLOW
    # --------------------------------------------------

    response_workflow = (
        response_orchestrator
        .generate_response_workflow(

            attack_type=
            normalized_attack,

            severity=
            severity,

            decision=
            decision,

            defense_state=
            defense_state,

            repeat_offender=
            repeat_offender
        )
    )

    # --------------------------------------------------
    # GET RECENT RESPONSE WORKFLOWS
    # --------------------------------------------------

    recent_workflows = (
        response_orchestrator
        .get_recent_workflows()
    )

    # --------------------------------------------------
    # GENERATE DEFENSE PLAYBOOK
    # --------------------------------------------------

    defense_playbook = (

        defense_playbook_engine
        .generate_playbook(

            attack_type=
            normalized_attack,

            severity=
            severity,

            decision=
            decision,

            defense_state=
            defense_state
        )
    )

    # --------------------------------------------------
    # GET PLAYBOOK HISTORY
    # --------------------------------------------------

    playbook_history = (

        defense_playbook_engine
        .get_playbook_history()
    )

    containment_statistics = (

        containment_engine
        .get_statistics()
    )

    # --------------------------------------------------
    # FINAL AI INTELLIGENCE RESPONSE
    # --------------------------------------------------

    response = {

        "ip_address":
        ip_address,

        "original_attack":
        attack_type,

        "normalized_attack":
        normalized_attack,

        "confidence":
        round(confidence, 4),

        # --------------------------------------------------
        # THREAT ANALYSIS
        # --------------------------------------------------

        "severity":
        severity,

        "reputation_score":
        reputation_score,

        "reputation_level":
        reputation_level,

        # --------------------------------------------------
        # DEFENSIVE STATE
        # --------------------------------------------------

        "defense_state":
        defense_state,

        # --------------------------------------------------
        # THREAT INTELLIGENCE
        # --------------------------------------------------

        "threat_profile":
        attacker_profile,

        # --------------------------------------------------
        # INCIDENT RESPONSE
        # --------------------------------------------------

        "incident_report":
        incident_report,

        # --------------------------------------------------
        # INCIDENT CENTER
        # --------------------------------------------------

        "incident":
        incident,

        "incident_statistics":
        incident_center.get_statistics(),

        # --------------------------------------------------
        # AI ACTION LOGS
        # --------------------------------------------------

        "recent_ai_logs":
        recent_ai_logs,

        # --------------------------------------------------
        # RESPONSE ORCHESTRATION
        # --------------------------------------------------

        "response_workflow":
        response_workflow,

        "recent_workflows":
        recent_workflows,

        # --------------------------------------------------
        # DEFENSE PLAYBOOKS
        # --------------------------------------------------

        "defense_playbook":
        defense_playbook,

        "playbook_history":
        playbook_history,

        # --------------------------------------------------
        # IPS DECISION
        # --------------------------------------------------

        "decision":
        decision,
        
        # --------------------------------------------------
        # ENFORCEMENT POLICY
        # --------------------------------------------------

        "enforcement_policy":
        enforcement_policy,


        # CONTAINMENT


        "containment_record":
        containment_record,

        "containment_statistics":
        containment_statistics,

        "enforcement_result":
        enforcement_result,

        # --------------------------------------------------
        # IPS STATUS
        # --------------------------------------------------

        "is_watchlisted":
        is_watchlisted,

        "is_temp_banned":
        is_temp_banned,

        "is_blocked":
        is_blocked,

        # --------------------------------------------------
        # MEMORY / BEHAVIOR
        # --------------------------------------------------

        "repeat_offender":
        repeat_offender,

        "attack_count":
        attacker_info["attack_count"],

        "unique_attacks":
        attacker_info["unique_attacks"],

        "first_seen":
        attacker_info["first_seen"],

        "last_seen":
        attacker_info["last_seen"],

        # --------------------------------------------------
        # AI ANALYSIS
        # --------------------------------------------------

        "recommendation":
        recommendation,

        "explanation":
        explanation
    }

    return response