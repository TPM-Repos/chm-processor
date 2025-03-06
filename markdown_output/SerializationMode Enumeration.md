       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SerializationMode Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : SerializationMode Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Controls the serialization of a control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum SerializationMode 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SerializationMode](topic7318.md)  
  
C#|   
---|---  
      
    
    public enum SerializationMode : System.Enum   
  
# Members

Member| Description  
---|---  
**Backup**|  Serializes the information required to backup the control.  
**Copy**|  Serializes the information required to duplicate the control.  
**Display**|  Serializes the information required to display the control to and end-user.  
**Save**|  Serializes the information required to save the control to a file as part of the project, and reload it when the project is loaded.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Forms.SerializationMode**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Forms Namespace](topic7266.md)


