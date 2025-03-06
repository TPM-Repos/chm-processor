SearchFinished Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameProcess Class](topic10287.md) : SearchFinished Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the search phase of the rename process has finished. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event SearchFinished As EventHandler(Of SearchFinishedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RenameProcess](topic10287.md)
    Dim handler As EventHandler(Of SearchFinishedEventArgs)
     
    AddHandler instance.SearchFinished, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SearchFinishedEventArgs> SearchFinished  
  
# Event Data

The event handler receives an argument of type [SearchFinishedEventArgs](topic10317.md) containing data related to this event. The following **SearchFinishedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Names](topic10324.md)| Gets the names that was searched for.   
[Uses](topic10325.md)| Gets all uses in rules of the name we searched for.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RenameProcess Class](topic10287.md)   
[RenameProcess Members](topic10288.md)


