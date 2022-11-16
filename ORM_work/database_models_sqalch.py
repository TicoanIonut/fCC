# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Numeric, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Country(Base):
    __tablename__ = 'Country'

    id = Column(Integer, primary_key=True)
    name = Column(Text)


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(Text)

class Player(Base):
    __tablename__ = 'Player'

    id = Column(Integer, primary_key=True)
    player_api_id = Column(Integer)
    player_name = Column(Text)
    player_fifa_api_id = Column(Integer)
    birthday = Column(Text)
    height = Column(Integer)
    weight = Column(Integer)


class Team(Base):
    __tablename__ = 'Team'

    id = Column(Integer, primary_key=True)
    team_api_id = Column(Integer)
    team_fifa_api_id = Column(Integer)
    team_long_name = Column(Text)
    team_short_name = Column(Text)





t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class League(Base):
    __tablename__ = 'League'

    id = Column(Integer, primary_key=True)
    country_id = Column(ForeignKey('country.id'))
    name = Column(Text)

    country = relationship('Country')


class PlayerAttribute(Base):
    __tablename__ = 'Player_Attributes'

    id = Column(Integer, primary_key=True)
    player_fifa_api_id = Column(ForeignKey('Player.player_fifa_api_id'))
    player_api_id = Column(ForeignKey('Player.player_api_id'))
    date = Column(Text)
    overall_rating = Column(Integer)
    potential = Column(Integer)
    preferred_foot = Column(Text)
    attacking_work_rate = Column(Text)
    defensive_work_rate = Column(Text)
    crossing = Column(Integer)
    finishing = Column(Integer)
    heading_accuracy = Column(Integer)
    short_passing = Column(Integer)
    volleys = Column(Integer)
    dribbling = Column(Integer)
    curve = Column(Integer)
    free_kick_accuracy = Column(Integer)
    long_passing = Column(Integer)
    ball_control = Column(Integer)
    acceleration = Column(Integer)
    sprint_speed = Column(Integer)
    agility = Column(Integer)
    reactions = Column(Integer)
    balance = Column(Integer)
    shot_power = Column(Integer)
    jumping = Column(Integer)
    stamina = Column(Integer)
    strength = Column(Integer)
    long_shots = Column(Integer)
    aggression = Column(Integer)
    interceptions = Column(Integer)
    positioning = Column(Integer)
    vision = Column(Integer)
    penalties = Column(Integer)
    marking = Column(Integer)
    standing_tackle = Column(Integer)
    sliding_tackle = Column(Integer)
    gk_diving = Column(Integer)
    gk_handling = Column(Integer)
    gk_kicking = Column(Integer)
    gk_positioning = Column(Integer)
    gk_reflexes = Column(Integer)

    player_api = relationship('Player', primaryjoin='PlayerAttribute.player_api_id == Player.player_api_id')
    player_fifa_api = relationship('Player', primaryjoin='PlayerAttribute.player_fifa_api_id == Player.player_fifa_api_id')


class TeamAttribute(Base):
    __tablename__ = 'Team_Attributes'

    id = Column(Integer, primary_key=True)
    team_fifa_api_id = Column(ForeignKey('Team.team_fifa_api_id'))
    team_api_id = Column(ForeignKey('Team.team_api_id'))
    date = Column(Text)
    buildUpPlaySpeed = Column(Integer)
    buildUpPlaySpeedClass = Column(Text)
    buildUpPlayDribbling = Column(Integer)
    buildUpPlayDribblingClass = Column(Text)
    buildUpPlayPassing = Column(Integer)
    buildUpPlayPassingClass = Column(Text)
    buildUpPlayPositioningClass = Column(Text)
    chanceCreationPassing = Column(Integer)
    chanceCreationPassingClass = Column(Text)
    chanceCreationCrossing = Column(Integer)
    chanceCreationCrossingClass = Column(Text)
    chanceCreationShooting = Column(Integer)
    chanceCreationShootingClass = Column(Text)
    chanceCreationPositioningClass = Column(Text)
    defencePressure = Column(Integer)
    defencePressureClass = Column(Text)
    defenceAggression = Column(Integer)
    defenceAggressionClass = Column(Text)
    defenceTeamWidth = Column(Integer)
    defenceTeamWidthClass = Column(Text)
    defenceDefenderLineClass = Column(Text)

    team_api = relationship('Team', primaryjoin='TeamAttribute.team_api_id == Team.team_api_id')
    team_fifa_api = relationship('Team', primaryjoin='TeamAttribute.team_fifa_api_id == Team.team_fifa_api_id')


class Match(Base):
    __tablename__ = 'Match'

    id = Column(Integer, primary_key=True)
    country_id = Column(ForeignKey('country.id'))
    league_id = Column(ForeignKey('League.id'))
    season = Column(Text)
    stage = Column(Integer)
    date = Column(Text)
    match_api_id = Column(Integer)
    home_team_api_id = Column(ForeignKey('Team.team_api_id'))
    away_team_api_id = Column(ForeignKey('Team.team_api_id'))
    home_team_goal = Column(Integer)
    away_team_goal = Column(Integer)
    home_player_X1 = Column(Integer)
    home_player_X2 = Column(Integer)
    home_player_X3 = Column(Integer)
    home_player_X4 = Column(Integer)
    home_player_X5 = Column(Integer)
    home_player_X6 = Column(Integer)
    home_player_X7 = Column(Integer)
    home_player_X8 = Column(Integer)
    home_player_X9 = Column(Integer)
    home_player_X10 = Column(Integer)
    home_player_X11 = Column(Integer)
    away_player_X1 = Column(Integer)
    away_player_X2 = Column(Integer)
    away_player_X3 = Column(Integer)
    away_player_X4 = Column(Integer)
    away_player_X5 = Column(Integer)
    away_player_X6 = Column(Integer)
    away_player_X7 = Column(Integer)
    away_player_X8 = Column(Integer)
    away_player_X9 = Column(Integer)
    away_player_X10 = Column(Integer)
    away_player_X11 = Column(Integer)
    home_player_Y1 = Column(Integer)
    home_player_Y2 = Column(Integer)
    home_player_Y3 = Column(Integer)
    home_player_Y4 = Column(Integer)
    home_player_Y5 = Column(Integer)
    home_player_Y6 = Column(Integer)
    home_player_Y7 = Column(Integer)
    home_player_Y8 = Column(Integer)
    home_player_Y9 = Column(Integer)
    home_player_Y10 = Column(Integer)
    home_player_Y11 = Column(Integer)
    away_player_Y1 = Column(Integer)
    away_player_Y2 = Column(Integer)
    away_player_Y3 = Column(Integer)
    away_player_Y4 = Column(Integer)
    away_player_Y5 = Column(Integer)
    away_player_Y6 = Column(Integer)
    away_player_Y7 = Column(Integer)
    away_player_Y8 = Column(Integer)
    away_player_Y9 = Column(Integer)
    away_player_Y10 = Column(Integer)
    away_player_Y11 = Column(Integer)
    home_player_1 = Column(ForeignKey('Player.player_api_id'))
    home_player_2 = Column(ForeignKey('Player.player_api_id'))
    home_player_3 = Column(ForeignKey('Player.player_api_id'))
    home_player_4 = Column(ForeignKey('Player.player_api_id'))
    home_player_5 = Column(ForeignKey('Player.player_api_id'))
    home_player_6 = Column(ForeignKey('Player.player_api_id'))
    home_player_7 = Column(ForeignKey('Player.player_api_id'))
    home_player_8 = Column(ForeignKey('Player.player_api_id'))
    home_player_9 = Column(ForeignKey('Player.player_api_id'))
    home_player_10 = Column(ForeignKey('Player.player_api_id'))
    home_player_11 = Column(ForeignKey('Player.player_api_id'))
    away_player_1 = Column(ForeignKey('Player.player_api_id'))
    away_player_2 = Column(ForeignKey('Player.player_api_id'))
    away_player_3 = Column(ForeignKey('Player.player_api_id'))
    away_player_4 = Column(ForeignKey('Player.player_api_id'))
    away_player_5 = Column(ForeignKey('Player.player_api_id'))
    away_player_6 = Column(ForeignKey('Player.player_api_id'))
    away_player_7 = Column(ForeignKey('Player.player_api_id'))
    away_player_8 = Column(ForeignKey('Player.player_api_id'))
    away_player_9 = Column(ForeignKey('Player.player_api_id'))
    away_player_10 = Column(ForeignKey('Player.player_api_id'))
    away_player_11 = Column(ForeignKey('Player.player_api_id'))
    goal = Column(Text)
    shoton = Column(Text)
    shotoff = Column(Text)
    foulcommit = Column(Text)
    card = Column(Text)
    cross = Column(Text)
    corner = Column(Text)
    possession = Column(Text)
    B365H = Column(Numeric)
    B365D = Column(Numeric)
    B365A = Column(Numeric)
    BWH = Column(Numeric)
    BWD = Column(Numeric)
    BWA = Column(Numeric)
    IWH = Column(Numeric)
    IWD = Column(Numeric)
    IWA = Column(Numeric)
    LBH = Column(Numeric)
    LBD = Column(Numeric)
    LBA = Column(Numeric)
    PSH = Column(Numeric)
    PSD = Column(Numeric)
    PSA = Column(Numeric)
    WHH = Column(Numeric)
    WHD = Column(Numeric)
    WHA = Column(Numeric)
    SJH = Column(Numeric)
    SJD = Column(Numeric)
    SJA = Column(Numeric)
    VCH = Column(Numeric)
    VCD = Column(Numeric)
    VCA = Column(Numeric)
    GBH = Column(Numeric)
    GBD = Column(Numeric)
    GBA = Column(Numeric)
    BSH = Column(Numeric)
    BSD = Column(Numeric)
    BSA = Column(Numeric)

    Player = relationship('Player', primaryjoin='Match.away_player_1 == Player.player_api_id')
    Player1 = relationship('Player', primaryjoin='Match.away_player_10 == Player.player_api_id')
    Player2 = relationship('Player', primaryjoin='Match.away_player_11 == Player.player_api_id')
    Player3 = relationship('Player', primaryjoin='Match.away_player_2 == Player.player_api_id')
    Player4 = relationship('Player', primaryjoin='Match.away_player_3 == Player.player_api_id')
    Player5 = relationship('Player', primaryjoin='Match.away_player_4 == Player.player_api_id')
    Player6 = relationship('Player', primaryjoin='Match.away_player_5 == Player.player_api_id')
    Player7 = relationship('Player', primaryjoin='Match.away_player_6 == Player.player_api_id')
    Player8 = relationship('Player', primaryjoin='Match.away_player_7 == Player.player_api_id')
    Player9 = relationship('Player', primaryjoin='Match.away_player_8 == Player.player_api_id')
    Player10 = relationship('Player', primaryjoin='Match.away_player_9 == Player.player_api_id')
    away_team_api = relationship('Team', primaryjoin='Match.away_team_api_id == Team.team_api_id')
    country = relationship('Country')
    Player11 = relationship('Player', primaryjoin='Match.home_player_1 == Player.player_api_id')
    Player12 = relationship('Player', primaryjoin='Match.home_player_10 == Player.player_api_id')
    Player13 = relationship('Player', primaryjoin='Match.home_player_11 == Player.player_api_id')
    Player14 = relationship('Player', primaryjoin='Match.home_player_2 == Player.player_api_id')
    Player15 = relationship('Player', primaryjoin='Match.home_player_3 == Player.player_api_id')
    Player16 = relationship('Player', primaryjoin='Match.home_player_4 == Player.player_api_id')
    Player17 = relationship('Player', primaryjoin='Match.home_player_5 == Player.player_api_id')
    Player18 = relationship('Player', primaryjoin='Match.home_player_6 == Player.player_api_id')
    Player19 = relationship('Player', primaryjoin='Match.home_player_7 == Player.player_api_id')
    Player20 = relationship('Player', primaryjoin='Match.home_player_8 == Player.player_api_id')
    Player21 = relationship('Player', primaryjoin='Match.home_player_9 == Player.player_api_id')
    home_team_api = relationship('Team', primaryjoin='Match.home_team_api_id == Team.team_api_id')
    league = relationship('League')
