       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveRange Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5925.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [XmlTemplateDocument Class](topic5909.md) : RemoveRange Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    Name of the range to be removed from the drive list.

Glossary Item Box

Removes a range from the list of ranges to be driven. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveRange( _
       ByVal _name_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [XmlTemplateDocument](topic5909.md)
    Dim name As String
     
    instance.RemoveRange(name)  
  
C#|   
---|---  
      
    
    public void RemoveRange( 
       string _name_
    )  
  
#### Parameters

 _name_
    Name of the range to be removed from the drive list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[XmlTemplateDocument Class](topic5909.md)   
[XmlTemplateDocument Members](topic5910.md)

©2024 DriveWorks Ltd. All Rights Reserved.
