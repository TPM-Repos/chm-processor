Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseCommentChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ProjectComponentRule Class](topic6198.md) : RaiseCommentChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_args_
    The arguments to pass to the event.

Glossary Item Box

Raises the [CommentChanged](topic6214.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaiseCommentChanged( _
       ByVal _args_ As [ValueChangedEventArgs(Of String)](topic5834.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentRule](topic6198.md)
    Dim args As [ValueChangedEventArgs(Of String)](topic5834.md)
     
    instance.RaiseCommentChanged(args)  
  
C#|   
---|---  
      
    
    protected void RaiseCommentChanged( 
       [ValueChangedEventArgs<string>](topic5834.md) _args_
    )  
  
#### Parameters

 _args_
    The arguments to pass to the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentRule Class](topic6198.md)   
[ProjectComponentRule Members](topic6199.md)


