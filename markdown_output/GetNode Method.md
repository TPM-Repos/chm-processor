Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNode Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [NodeRef Class](topic12909.md) : GetNode Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    The project from which to retrieve the node.

Glossary Item Box

Gets the node from the specified project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Function GetNode( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [IFlowNode](topic6873.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeRef](topic12909.md)
    Dim project As [Project](topic3859.md)
    Dim value As [IFlowNode](topic6873.md)
     
    value = instance.GetNode(project)  
  
C#|   
---|---  
      
    
    public virtual [IFlowNode](topic6873.md) GetNode( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    The project from which to retrieve the node.

#### Return Value

The node in the project.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeRef Class](topic12909.md)   
[NodeRef Members](topic12910.md)


