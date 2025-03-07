Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Generate Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : Generate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Generates the file format and any additional files too. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function Generate() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim value As Boolean
     
    value = instance.Generate()  
  
C#|   
---|---  
      
    
    public abstract bool Generate()  
  
#### Return Value

Whether or not the generation process was a success.

# Remarks

failures should be reported.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)


