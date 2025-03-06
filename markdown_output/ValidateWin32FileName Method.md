ValidateWin32FileName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateWin32FileName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fileName_
    The name of the file without extension or path to validate.

Glossary Item Box

Validates a file name 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateWin32FileName( _
       ByVal _fileName_ As String _
    ) As [ValidatePathResult](topic13194.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim fileName As String
    Dim value As [ValidatePathResult](topic13194.md)
     
    value = [ValidationUtility](topic13287.md).ValidateWin32FileName(fileName)  
  
C#|   
---|---  
      
    
    public static [ValidatePathResult](topic13194.md) ValidateWin32FileName( 
       string _fileName_
    )  
  
#### Parameters

 _fileName_
    The name of the file without extension or path to validate.

#### Return Value

True if the path validates correctly, and false otherwise.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


