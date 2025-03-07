Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FrameRendered Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPreviewControl Interface](topic362.md) : FrameRendered Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever an image of the preview has finished displaying in the control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event FrameRendered As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewControl](topic362.md)
    Dim handler As EventHandler
     
    AddHandler instance.FrameRendered, handler  
  
C#|   
---|---  
      
    
    event EventHandler FrameRendered  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewControl Interface](topic362.md)   
[IPreviewControl Members](topic363.md)


