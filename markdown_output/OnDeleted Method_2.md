Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnDeleted Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ContainerControlBase Class](topic7684.md) : OnDeleted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    The event data.

Glossary Item Box

Raises the [Deleted](topic7759.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub OnDeleted( _
       ByVal _e_ As EventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ContainerControlBase](topic7684.md)
    Dim e As EventArgs
     
    instance.OnDeleted(e)  
  
C#|   
---|---  
      
    
    protected override void OnDeleted( 
       EventArgs _e_
    )  
  
#### Parameters

 _e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ContainerControlBase Class](topic7684.md)   
[ContainerControlBase Members](topic7685.md)


