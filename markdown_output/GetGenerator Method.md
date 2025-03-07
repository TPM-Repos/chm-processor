Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetGenerator Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FormatGeneratorFactory Class](topic13670.md) : GetGenerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_extension_
    The file extension to get the generator for e.g. ".pdf"

Glossary Item Box

Gets a generator from the specified file extension. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetGenerator( _
       ByVal _extension_ As String _
    ) As [FileFormatGenerator](topic13579.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FormatGeneratorFactory](topic13670.md)
    Dim extension As String
    Dim value As [FileFormatGenerator](topic13579.md)
     
    value = instance.GetGenerator(extension)  
  
C#|   
---|---  
      
    
    public [FileFormatGenerator](topic13579.md) GetGenerator( 
       string _extension_
    )  
  
#### Parameters

 _extension_
    The file extension to get the generator for e.g. ".pdf"

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FormatGeneratorFactory Class](topic13670.md)   
[FormatGeneratorFactory Members](topic13671.md)


