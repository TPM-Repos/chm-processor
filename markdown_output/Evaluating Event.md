Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Evaluating Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPendingChangesService Interface](topic355.md) : Evaluating Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when pending changes are being checked. use this event to register unsaved changes and their applicators. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Evaluating As EventHandler(Of PendingChangeEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPendingChangesService](topic355.md)
    Dim handler As EventHandler(Of PendingChangeEventArgs)
     
    AddHandler instance.Evaluating, handler  
  
C#|   
---|---  
      
    
    event EventHandler<PendingChangeEventArgs> Evaluating  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPendingChangesService Interface](topic355.md)   
[IPendingChangesService Members](topic356.md)


