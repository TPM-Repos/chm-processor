Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAllowedFileExtensions Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [UploadControl Class](topic9323.md) : GetAllowedFileExtensions Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a list of extensions for the files that are allowed to be uploaded with this control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetAllowedFileExtensions() As HashSet(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [UploadControl](topic9323.md)
    Dim value As HashSet(Of String)
     
    value = instance.GetAllowedFileExtensions()  
  
C#|   
---|---  
      
    
    public HashSet<string> GetAllowedFileExtensions()  
  
#### Return Value

A collection of extensions parsed from the [FileFilter](topic9335.md) property.

# Remarks

The Hashset is case insensitive.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[UploadControl Class](topic9323.md)   
[UploadControl Members](topic9324.md)


