Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTable Class](topic3926.md) : GetName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name to convert.

Glossary Item Box

Gets the invariant name of the table from a display name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetName( _
       ByVal _displayName_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim displayName As String
    Dim value As String
     
    value = [ProjectCalculationTable](topic3926.md).GetName(displayName)  
  
C#|   
---|---  
      
    
    public static string GetName( 
       string _displayName_
    )  
  
#### Parameters

 _displayName_
    The display name to convert.

#### Return Value

The converted name.

# Remarks

This just removes spaces.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTable Class](topic3926.md)   
[ProjectCalculationTable Members](topic3927.md)


