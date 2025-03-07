Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetDataFromClipboard Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ClipboardSupport Class](topic13507.md) : GetDataFromClipboard Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Retrieves the data from the clipboard. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetDataFromClipboard() As String(,)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value() As String
     
    value = [ClipboardSupport](topic13507.md).GetDataFromClipboard()  
  
C#|   
---|---  
      
    
    public static string[,] GetDataFromClipboard()  
  
#### Return Value

A two dimensional array of data from the clipboard.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ClipboardSupport Class](topic13507.md)   
[ClipboardSupport Members](topic13508.md)


