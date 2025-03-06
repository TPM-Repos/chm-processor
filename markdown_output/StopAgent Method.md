       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StopAgent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : StopAgent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_agentName_
    The name of the agent to be stopped.

Glossary Item Box

Stops an agent. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub StopAgent( _
       ByVal _agentName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim agentName As String
     
    instance.StopAgent(agentName)  
  
C#|   
---|---  
      
    
    public void StopAgent( 
       string _agentName_
    )  
  
#### Parameters

 _agentName_
    The name of the agent to be stopped.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


