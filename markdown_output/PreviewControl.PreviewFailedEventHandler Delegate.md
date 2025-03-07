Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviewControl.PreviewFailedEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : PreviewControl.PreviewFailedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    

_e_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub PreviewControl.PreviewFailedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [PreviewExceptionEventArgs](topic3811.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [PreviewControl.PreviewFailedEventHandler](topic9368.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void PreviewControl.PreviewFailedEventHandler( 
       object _sender_ ,
       [PreviewExceptionEventArgs](topic3811.md) _e_
    )  
  
#### Parameters

 _sender_
    
_e_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreviewControl.PreviewFailedEventHandler Members](topic9368.md)   
[DriveWorks.Forms Namespace](topic7266.md)


