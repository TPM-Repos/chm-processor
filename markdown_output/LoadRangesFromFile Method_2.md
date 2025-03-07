Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LoadRangesFromFile Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [XmlTemplateDocument Class](topic5909.md) : LoadRangesFromFile Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_overwrite_
    If the ranges from the file should overwrite the existing ones.

Glossary Item Box

Matches range information with ranges from file. Creates missing ranges and removes unused ones. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub LoadRangesFromFile( _
       ByVal _overwrite_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [XmlTemplateDocument](topic5909.md)
    Dim overwrite As Boolean
     
    instance.LoadRangesFromFile(overwrite)  
  
C#|   
---|---  
      
    
    public void LoadRangesFromFile( 
       bool _overwrite_
    )  
  
#### Parameters

 _overwrite_
    If the ranges from the file should overwrite the existing ones.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[XmlTemplateDocument Class](topic5909.md)   
[XmlTemplateDocument Members](topic5910.md)


