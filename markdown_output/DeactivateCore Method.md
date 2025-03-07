Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeactivateCore Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : DeactivateCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_cancel_
    The view should set this value to true before exiting the method if the view wishes to cancel the view switch.

Glossary Item Box

When overridden by a derived class, performs deactivation logic specific to the derived view. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub DeactivateCore( _
       ByRef _cancel_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim cancel As Boolean
     
    instance.DeactivateCore(cancel)  
  
C#|   
---|---  
      
    
    protected virtual void DeactivateCore( 
       ref bool _cancel_
    )  
  
#### Parameters

 _cancel_
    The view should set this value to true before exiting the method if the view wishes to cancel the view switch.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)


