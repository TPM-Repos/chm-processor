Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PictureSizeMode Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : PictureSizeMode Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies the behaviour used to size a picture in a picture box. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum PictureSizeMode 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PictureSizeMode](topic7311.md)  
  
C#|   
---|---  
      
    
    public enum PictureSizeMode : System.Enum   
  
# Members

Member| Description  
---|---  
**Center**|  Center the picture  
**Normal**|  Use the pictures native size  
**StretchImage**|  Size the picture to fit the picture box and ignore the aspect ratio of the picture.  
**Zoom**|  Size the picture to fit the picture box but preserve the aspect ratio of the picture.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Forms.PictureSizeMode**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Forms Namespace](topic7266.md)


