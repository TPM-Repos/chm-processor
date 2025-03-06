       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetDisplayName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4406.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocumentRule Class](topic4399.md) : SetDisplayName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newDisplayName_
    The new display name to apply.

Glossary Item Box

Sets the display name, see remarks for details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetDisplayName( _
       ByVal _newDisplayName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocumentRule](topic4399.md)
    Dim newDisplayName As String
     
    instance.SetDisplayName(newDisplayName)  
  
C#|   
---|---  
      
    
    public void SetDisplayName( 
       string _newDisplayName_
    )  
  
#### Parameters

 _newDisplayName_
    The new display name to apply.

# Remarks

If the new display name is empty or a null reference, then the display name returned by the [DisplayName](topic4409.md) property will be the same as the [Id](topic4411.md) property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocumentRule Class](topic4399.md)   
[ProjectDocumentRule Members](topic4400.md)

©2024 DriveWorks Ltd. All Rights Reserved.
