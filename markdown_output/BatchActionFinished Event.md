Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BatchActionFinished Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameProcess Class](topic10287.md) : BatchActionFinished Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an action affecting a batch of related rules is finished, e.g. loading rules for variables. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event BatchActionFinished As EventHandler(Of BatchActionEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RenameProcess](topic10287.md)
    Dim handler As EventHandler(Of BatchActionEventArgs)
     
    AddHandler instance.BatchActionFinished, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<BatchActionEventArgs> BatchActionFinished  
  
# Event Data

The event handler receives an argument of type [BatchActionEventArgs](topic10269.md) containing data related to this event. The following **BatchActionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Action](topic10275.md)| Gets the type of batch action.   
[TargetName](topic10276.md)| Gets the name of the target being affected by the action.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RenameProcess Class](topic10287.md)   
[RenameProcess Members](topic10288.md)


