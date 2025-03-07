Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAgentLog Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : GetAgentLog Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_agentName_
    The name of the agent whose message log is to be returned.

Glossary Item Box

Gets the agent message log of an agent. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetAgentLog( _
       ByVal _agentName_ As String _
    ) As IEnumerable(Of AgentLogEntry)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim agentName As String
    Dim value As IEnumerable(Of AgentLogEntry)
     
    value = instance.GetAgentLog(agentName)  
  
C#|   
---|---  
      
    
    public IEnumerable<AgentLogEntry> GetAgentLog( 
       string _agentName_
    )  
  
#### Parameters

 _agentName_
    The name of the agent whose message log is to be returned.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


