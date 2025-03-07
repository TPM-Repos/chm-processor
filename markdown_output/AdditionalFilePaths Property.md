Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFilePaths Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewResult Class](topic8817.md) : AdditionalFilePaths Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets a list of locations to find supporting files for the 3D Preview. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DataMemberAttribute()>
    Public Property AdditionalFilePaths As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PreviewResult](topic8817.md)
    Dim value() As String
     
    instance.AdditionalFilePaths = value
     
    value = instance.AdditionalFilePaths  
  
C#|   
---|---  
      
    
    [DataMemberAttribute()]
    public string[] AdditionalFilePaths {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreviewResult Class](topic8817.md)   
[PreviewResult Members](topic8818.md)


