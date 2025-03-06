       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateWin32FileNameWithPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateWin32FileNameWithPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fileNameWithPath_
    The name of the file with its path and extension to validate.

Glossary Item Box

Validates a full file path according to NTFS guidelines. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateWin32FileNameWithPath( _
       ByVal _fileNameWithPath_ As String _
    ) As [ValidatePathResult](topic13194.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim fileNameWithPath As String
    Dim value As [ValidatePathResult](topic13194.md)
     
    value = [ValidationUtility](topic13287.md).ValidateWin32FileNameWithPath(fileNameWithPath)  
  
C#|   
---|---  
      
    
    public static [ValidatePathResult](topic13194.md) ValidateWin32FileNameWithPath( 
       string _fileNameWithPath_
    )  
  
#### Parameters

 _fileNameWithPath_
    The name of the file with its path and extension to validate.

#### Return Value

True if the path validates correctly, and false otherwise.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


