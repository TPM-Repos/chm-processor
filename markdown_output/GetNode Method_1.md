Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNode Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [StartNodeRef Class](topic13140.md) : GetNode Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function GetNode( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [IFlowNode](topic6873.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StartNodeRef](topic13140.md)
    Dim project As [Project](topic3859.md)
    Dim value As [IFlowNode](topic6873.md)
     
    value = instance.GetNode(project)  
  
C#|   
---|---  
      
    
    public override [IFlowNode](topic6873.md) GetNode( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StartNodeRef Class](topic13140.md)   
[StartNodeRef Members](topic13141.md)


