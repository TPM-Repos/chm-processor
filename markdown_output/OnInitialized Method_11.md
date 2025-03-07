Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnInitialized Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewControl Class](topic8709.md) : OnInitialized Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    The event data.

Glossary Item Box

Raises the [ControlBase.Initialized](topic7760.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides NotOverridable Sub OnInitialized( _
       ByVal _e_ As EventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PreviewControl](topic8709.md)
    Dim e As EventArgs
     
    instance.OnInitialized(e)  
  
C#|   
---|---  
      
    
    protected override void OnInitialized( 
       EventArgs _e_
    )  
  
#### Parameters

 _e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreviewControl Class](topic8709.md)   
[PreviewControl Members](topic8710.md)


