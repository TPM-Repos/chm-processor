Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DefaultProperties Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : DefaultProperties Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of default properties that should be used when inheriting this class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Shared ReadOnly Property DefaultProperties As [FileFormatParameterInfo()](topic13615.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value() As [FileFormatParameterInfo](topic13615.md)
     
    value = [FileFormatGenerator](topic13579.md).DefaultProperties  
  
C#|   
---|---  
      
    
    protected static [FileFormatParameterInfo[]](topic13615.md) DefaultProperties {get;}  
  
# Remarks

This includes the file name and relative path parameters.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)


