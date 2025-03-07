Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DxfExportPath Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [GenerationSettings Class](topic15238.md) : DxfExportPath Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the path to a folder to which all exported DXFs should be saved, or a null reference to save them to the same location as their drawings. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property DxfExportPath As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationSettings](topic15238.md)
    Dim value As String
     
    instance.DxfExportPath = value
     
    value = instance.DxfExportPath  
  
C#|   
---|---  
      
    
    public string DxfExportPath {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationSettings Class](topic15238.md)   
[GenerationSettings Members](topic15239.md)


