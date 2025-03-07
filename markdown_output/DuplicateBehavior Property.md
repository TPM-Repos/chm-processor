Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DuplicateBehavior Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [CaptureImportManager Class](topic2468.md) : DuplicateBehavior Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the default behavior for duplicated items. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property DuplicateBehavior As [CaptureImportDuplicateBehavior](topic2345.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CaptureImportManager](topic2468.md)
    Dim value As [CaptureImportDuplicateBehavior](topic2345.md)
     
    instance.DuplicateBehavior = value
     
    value = instance.DuplicateBehavior  
  
C#|   
---|---  
      
    
    public [CaptureImportDuplicateBehavior](topic2345.md) DuplicateBehavior {get; set;}  
  
# Remarks

The default value of this property is [CaptureImportDuplicateBehavior.Replace](topic2345.md)

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CaptureImportManager Class](topic2468.md)   
[CaptureImportManager Members](topic2469.md)


