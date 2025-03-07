Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OperationInvoking Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : OperationInvoking Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a operation is about to be invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event OperationInvoking As [OperationEventHandler](topic11820.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [OperationEventHandler](topic11820.md)
     
    AddHandler instance.OperationInvoking, handler  
  
C#|   
---|---  
      
    
    public event [OperationEventHandler](topic11820.md) OperationInvoking  
  
# Event Data

The event handler receives an argument of type [OperationEventArgs](topic11084.md) containing data related to this event. The following **OperationEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Operation](topic11094.md)| Gets the operation which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


