       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdateSpecificationDirectory Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3406.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : TryUpdateSpecificationDirectory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The identification of the specification to update.

_newPath_
    The new specification directory.

Glossary Item Box

Attempts to update the specifications location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateSpecificationDirectory( _
       ByVal _specificationId_ As Integer, _
       ByVal _newPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim newPath As String
    Dim value As Boolean
     
    value = instance.TryUpdateSpecificationDirectory(specificationId, newPath)  
  
C#|   
---|---  
      
    
    public bool TryUpdateSpecificationDirectory( 
       int _specificationId_ ,
       string _newPath_
    )  
  
#### Parameters

 _specificationId_
    The identification of the specification to update.
_newPath_
    The new specification directory.

#### Return Value

True if the specification directory was successfully updated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
