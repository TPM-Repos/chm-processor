Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ClipboardContains Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ClipboardSupport Class](topic13507.md) : ClipboardContains Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_clipboardType_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ClipboardContains( _
       ByVal _clipboardType_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim clipboardType As String
    Dim value As Boolean
     
    value = [ClipboardSupport](topic13507.md).ClipboardContains(clipboardType)  
  
C#|   
---|---  
      
    
    public static bool ClipboardContains( 
       string _clipboardType_
    )  
  
#### Parameters

 _clipboardType_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ClipboardSupport Class](topic13507.md)   
[ClipboardSupport Members](topic13508.md)


