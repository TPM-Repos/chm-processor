       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateWin32Path Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateWin32Path Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_path_
    The path to validate

Glossary Item Box

Validates a path according to NTFS guidelines 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateWin32Path( _
       ByVal _path_ As String _
    ) As [ValidatePathResult](topic13194.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim path As String
    Dim value As [ValidatePathResult](topic13194.md)
     
    value = [ValidationUtility](topic13287.md).ValidateWin32Path(path)  
  
C#|   
---|---  
      
    
    public static [ValidatePathResult](topic13194.md) ValidateWin32Path( 
       string _path_
    )  
  
#### Parameters

 _path_
    The path to validate

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


