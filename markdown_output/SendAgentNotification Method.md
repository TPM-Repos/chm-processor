       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SendAgentNotification Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2978.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : SendAgentNotification Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_agentName_
    Name of the agent to send the message to

_message_
    The notification to send to the agent. Object type MUST be marked with System.SerializableAttribute.

Glossary Item Box

Attempts to send a notification message to the specified agent. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SendAgentNotification( _
       ByVal _agentName_ As String, _
       ByVal _message_ As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim agentName As String
    Dim message As Object
     
    instance.SendAgentNotification(agentName, message)  
  
C#|   
---|---  
      
    
    public void SendAgentNotification( 
       string _agentName_ ,
       object _message_
    )  
  
#### Parameters

 _agentName_
    Name of the agent to send the message to
 _message_
    The notification to send to the agent. Object type MUST be marked with System.SerializableAttribute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)

©2024 DriveWorks Ltd. All Rights Reserved.
