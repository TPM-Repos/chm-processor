Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnSelectedItemsChanged Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : OnSelectedItemsChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    The event data.

Glossary Item Box

Raises the [SelectedItemsChanged](topic1153.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnSelectedItemsChanged( _
       ByVal _e_ As [SelectionChangeEventArgs](topic926.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim e As [SelectionChangeEventArgs](topic926.md)
     
    instance.OnSelectedItemsChanged(e)  
  
C#|   
---|---  
      
    
    protected virtual void OnSelectedItemsChanged( 
       [SelectionChangeEventArgs](topic926.md) _e_
    )  
  
#### Parameters

 _e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)


