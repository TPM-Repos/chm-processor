![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddAgentLogEntry Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2964.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : AddAgentLogEntry Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_agentName_
    The name of the agent who the log entry originates from.

_dateAndTime_
    The date and time of the event.

_sourceDisplayName_
    The display name of the source of the event.

_targetDisplayName_
    The display name of the target of the event.

_description_
    The description of the event.

_type_
    

Glossary Item Box

Adds an agent log entry. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddAgentLogEntry( _
       ByVal _agentName_ As String, _
       ByVal _dateAndTime_ As String, _
       ByVal _sourceDisplayName_ As String, _
       ByVal _targetDisplayName_ As String, _
       ByVal _description_ As String, _
       ByVal _type_ As Integer _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim agentName As String
    Dim dateAndTime As String
    Dim sourceDisplayName As String
    Dim targetDisplayName As String
    Dim description As String
    Dim type As Integer
     
    instance.AddAgentLogEntry(agentName, dateAndTime, sourceDisplayName, targetDisplayName, description, type)  
  
C#|   
---|---  
      
    
    public void AddAgentLogEntry( 
       string _agentName_ ,
       string _dateAndTime_ ,
       string _sourceDisplayName_ ,
       string _targetDisplayName_ ,
       string _description_ ,
       int _type_
    )  
  
#### Parameters

 _agentName_
    The name of the agent who the log entry originates from.
_dateAndTime_
    The date and time of the event.
_sourceDisplayName_
    The display name of the source of the event.
_targetDisplayName_
    The display name of the target of the event.
_description_
    The description of the event.
_type_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)

©2024 DriveWorks Ltd. All Rights Reserved.
