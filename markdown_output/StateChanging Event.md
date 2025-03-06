StateChanging Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : StateChanging Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a state is about to be changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event StateChanging As [StateChangeEventHandler](topic11824.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [StateChangeEventHandler](topic11824.md)
     
    AddHandler instance.StateChanging, handler  
  
C#|   
---|---  
      
    
    public event [StateChangeEventHandler](topic11824.md) StateChanging  
  
# Event Data

The event handler receives an argument of type [StateChangeEventArgs](topic11578.md) containing data related to this event. The following **StateChangeEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[SourceState](topic11588.md)| Gets the state which is the source of the event.   
[TargetState](topic11589.md)| Gets the state which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


