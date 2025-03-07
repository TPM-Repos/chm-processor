Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCollection Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [NodeCollectionRef Class](topic12900.md) : GetCollection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    The project to retrieve the collection from.

Glossary Item Box

Gets the collection from the specified project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetCollection( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [FlowNodeCollection](topic7011.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeCollectionRef](topic12900.md)
    Dim project As [Project](topic3859.md)
    Dim value As [FlowNodeCollection](topic7011.md)
     
    value = instance.GetCollection(project)  
  
C#|   
---|---  
      
    
    public abstract [FlowNodeCollection](topic7011.md) GetCollection( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    The project to retrieve the collection from.

#### Return Value

The collection this reference refers to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeCollectionRef Class](topic12900.md)   
[NodeCollectionRef Members](topic12901.md)


