Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OperationDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Operations Class](topic11095.md) : OperationDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when an operation is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event OperationDeleted As [OperationEventHandler](topic11820.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Operations](topic11095.md)
    Dim handler As [OperationEventHandler](topic11820.md)
     
    AddHandler instance.OperationDeleted, handler  
  
C#|   
---|---  
      
    
    public event [OperationEventHandler](topic11820.md) OperationDeleted  
  
# Event Data

The event handler receives an argument of type [OperationEventArgs](topic11084.md) containing data related to this event. The following **OperationEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Operation](topic11094.md)| Gets the operation which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Operations Class](topic11095.md)   
[Operations Members](topic11096.md)


