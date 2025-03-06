       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RenameItem Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8845.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [RenameItem Class](topic8839.md) : RenameItem Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldName_
    Name to replace.

_newName_
    Replacement name.

Glossary Item Box

Creates a new instance of the [RenameItem](topic8839.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _oldName_ As String, _
       ByVal _newName_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim oldName As String
    Dim newName As String
     
    Dim instance As New [RenameItem](topic8839.md)(oldName, newName)  
  
C#|   
---|---  
      
    
    public RenameItem( 
       string _oldName_ ,
       string _newName_
    )  
  
#### Parameters

 _oldName_
    Name to replace.
_newName_
    Replacement name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RenameItem Class](topic8839.md)   
[RenameItem Members](topic8840.md)

©2024 DriveWorks Ltd. All Rights Reserved.
