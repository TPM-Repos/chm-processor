Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ActivateCore Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : ActivateCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_firstShow_
    True if it is the first time the view control has been shown.

_cancel_
    Set to true by the overridden method to cancel to navigation action if desired.

Glossary Item Box

When overridden by a derived class, performs activation logic specific to the derived view. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub ActivateCore( _
       ByVal _firstShow_ As Boolean, _
       ByRef _cancel_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim firstShow As Boolean
    Dim cancel As Boolean
     
    instance.ActivateCore(firstShow, cancel)  
  
C#|   
---|---  
      
    
    protected virtual void ActivateCore( 
       bool _firstShow_ ,
       ref bool _cancel_
    )  
  
#### Parameters

 _firstShow_
    True if it is the first time the view control has been shown.
_cancel_
    Set to true by the overridden method to cancel to navigation action if desired.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)


