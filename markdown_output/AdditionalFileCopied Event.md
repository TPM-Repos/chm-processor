Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFileCopied Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : AdditionalFileCopied Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the additional file format has been copied to the target location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event AdditionalFileCopied As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.AdditionalFileCopied, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> AdditionalFileCopied  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)


