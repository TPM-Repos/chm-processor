![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SendAgentRequest Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2979.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : SendAgentRequest Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_agentName_
    The name of the agent to send the request message to.

_message_
    The request to send to the specified agent. Object type MUST be marked with System.SerializableAttribute.

Glossary Item Box

Attempts to send a request message to the specified agent. Then waits for a reply and returns that result. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function SendAgentRequest( _
       ByVal _agentName_ As String, _
       ByVal _message_ As Object _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim agentName As String
    Dim message As Object
    Dim value As Object
     
    value = instance.SendAgentRequest(agentName, message)  
  
C#|   
---|---  
      
    
    public object SendAgentRequest( 
       string _agentName_ ,
       object _message_
    )  
  
#### Parameters

 _agentName_
    The name of the agent to send the request message to.
_message_
    The request to send to the specified agent. Object type MUST be marked with System.SerializableAttribute.

#### Return Value

The reply value from the agent.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)

©2024 DriveWorks Ltd. All Rights Reserved.
