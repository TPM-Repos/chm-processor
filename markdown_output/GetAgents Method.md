Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAgents Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : GetAgents Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a list of generated agents in the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetAgents() As IEnumerable(Of AgentDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim value As IEnumerable(Of AgentDetails)
     
    value = instance.GetAgents()  
  
C#|   
---|---  
      
    
    public IEnumerable<AgentDetails> GetAgents()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


