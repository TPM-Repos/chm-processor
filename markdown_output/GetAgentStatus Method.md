Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAgentStatus Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : GetAgentStatus Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_agentName_
    The name of the agent whose status is to be returned.

Glossary Item Box

Gets status information of an agent. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetAgentStatus( _
       ByVal _agentName_ As String _
    ) As [AutopilotAgentStatus](topic2414.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim agentName As String
    Dim value As [AutopilotAgentStatus](topic2414.md)
     
    value = instance.GetAgentStatus(agentName)  
  
C#|   
---|---  
      
    
    public [AutopilotAgentStatus](topic2414.md) GetAgentStatus( 
       string _agentName_
    )  
  
#### Parameters

 _agentName_
    The name of the agent whose status is to be returned.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


