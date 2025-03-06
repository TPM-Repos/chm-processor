       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14942.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedFormatCollection Class](topic14934.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_format_
    The format to remove from the collection.

Glossary Item Box

Removes the given format from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _format_ As [ReleasedFormat](topic14925.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedFormatCollection](topic14934.md)
    Dim format As [ReleasedFormat](topic14925.md)
    Dim value As Boolean
     
    value = instance.Remove(format)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [ReleasedFormat](topic14925.md) _format_
    )  
  
#### Parameters

 _format_
    The format to remove from the collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedFormatCollection Class](topic14934.md)   
[ReleasedFormatCollection Members](topic14935.md)

©2024 DriveWorks Ltd. All Rights Reserved.
