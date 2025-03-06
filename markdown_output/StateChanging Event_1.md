StateChanging Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IHasState Interface](topic300.md) : StateChanging Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the current state of the object is about to change. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event StateChanging As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasState](topic300.md)
    Dim handler As EventHandler
     
    AddHandler instance.StateChanging, handler  
  
C#|   
---|---  
      
    
    event EventHandler StateChanging  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasState Interface](topic300.md)   
[IHasState Members](topic301.md)


